param([string]$CommandFile)
$ErrorActionPreference = 'Stop'
Add-Type -TypeDefinition @'
using System;
using System.Text;
using System.Runtime.InteropServices;
public class AD {
 [StructLayout(LayoutKind.Sequential)] public struct RECT { public int Left,Top,Right,Bottom; }
 public delegate bool EnumProc(IntPtr h, IntPtr p);
 [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
 [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
 [DllImport("user32.dll")] public static extern bool ShowWindowAsync(IntPtr h,int c);
 [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
 [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
 [DllImport("user32.dll")] public static extern IntPtr GetLastActivePopup(IntPtr h);
 [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h,out RECT r);
 [DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);
 [DllImport("user32.dll")] public static extern void mouse_event(uint f,uint x,uint y,uint d,UIntPtr e);
 [DllImport("user32.dll")] public static extern void keybd_event(byte k,byte s,uint f,UIntPtr e);
 [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h,out uint p);
 [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr h,EnumProc f,IntPtr p);
 [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f,IntPtr p);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h,StringBuilder s,int n);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr h,StringBuilder s,int n);
 [DllImport("user32.dll")] public static extern int GetDlgCtrlID(IntPtr h);
 [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)] public static extern IntPtr SendMessage(IntPtr h,uint m,IntPtr w,string l);
}
'@
[void][AD]::SetProcessDPIAware()
[void][AD]::SetThreadDpiAwarenessContext([IntPtr](-4))
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
$run = Split-Path $PSScriptRoot -Parent
$cfg = Get-Content -LiteralPath $CommandFile -Raw | ConvertFrom-Json
$proc = Get-Process -Name Aspire | Where-Object {$_.MainWindowHandle -ne 0} | Select-Object -First 1
if (!$proc) { throw 'No running Aspire window.' }
$hwnd = $proc.MainWindowHandle
$script:actualMain=[IntPtr]::Zero
$findMain=[AD+EnumProc]{param($h,$p)
 [uint32]$wp=0;[void][AD]::GetWindowThreadProcessId($h,[ref]$wp)
 if($wp -eq $proc.Id){$t=New-Object Text.StringBuilder 1024;[void][AD]::GetWindowText($h,$t,1024);if($t.ToString().StartsWith('Aspire ')){$script:actualMain=$h}}
 return $true
}
[void][AD]::EnumWindows($findMain,[IntPtr]::Zero)
if($script:actualMain -ne [IntPtr]::Zero){$hwnd=$script:actualMain}
$dialogs=@(Get-Process -Name SandboxedFileDialog -ErrorAction SilentlyContinue | Where-Object {$_.Path -eq 'C:\Program Files\Aspire 12.5\x64\SandboxedFileDialog.exe'})
$allowedPids=@($proc.Id)+@($dialogs | ForEach-Object {$_.Id})
$focusProcess=$proc
if($dialogs.Count -gt 0){$focusProcess=$dialogs | Where-Object {$_.MainWindowHandle -ne 0} | Select-Object -First 1;if(!$focusProcess){$focusProcess=$proc}}
[void](New-Object -ComObject WScript.Shell).AppActivate($focusProcess.Id)
$focusHandle=[AD]::GetLastActivePopup($hwnd)
if($focusProcess.Id -ne $proc.Id){$focusHandle=$focusProcess.MainWindowHandle}
[void][AD]::SetForegroundWindow($focusHandle)
Start-Sleep -Milliseconds 500
function Key([string]$combo) {
 $map=@{CTRL=17;ALT=18;SHIFT=16;ENTER=13;ESC=27;TAB=9;DELETE=46;BACKSPACE=8;F4=115;F9=120;F12=123;HOME=36;END=35;LEFT=37;UP=38;RIGHT=39;DOWN=40;SPACE=32}
 $keys=@($combo.ToUpper().Split('+') | ForEach-Object { if($map.ContainsKey($_)){$map[$_]}elseif($_ -match '^F([1-9]|1[0-2])$'){111+[int]$Matches[1]}elseif($_.Length -eq 1){[int][char]$_}else{throw "Unknown key $_"} })
 foreach($k in $keys){[AD]::keybd_event([byte]$k,0,0,[UIntPtr]::Zero)}
 Start-Sleep -Milliseconds 45
 [array]::Reverse($keys)
 foreach($k in $keys){[AD]::keybd_event([byte]$k,0,2,[UIntPtr]::Zero)}
}
function FindControl([int]$id,[string]$class) {
 $script:matches=New-Object System.Collections.Generic.List[object]
 $find=[AD+EnumProc]{param($h,$p)
  if([AD]::IsWindowVisible($h) -and [AD]::GetDlgCtrlID($h) -eq $id){
   $c=New-Object Text.StringBuilder 256;[void][AD]::GetClassName($h,$c,256)
   if($c.ToString() -eq $class){$script:matches.Add($h)}
  };return $true
 }
 $scope=[AD]::GetLastActivePopup($hwnd)
 [void][AD]::EnumChildWindows($scope,$find,[IntPtr]::Zero)
 if($script:matches.Count -ne 1){throw "Expected one visible $class with ID $id, found $($script:matches.Count)"}
 return $script:matches[0]
}
foreach($a in $cfg.actions) {
 [uint32]$foregroundPid=0
 [void][AD]::GetWindowThreadProcessId([AD]::GetForegroundWindow(),[ref]$foregroundPid)
 if($a.type -ne 'wait' -and $allowedPids -notcontains $foregroundPid){
  $newDialog=Get-Process -Id $foregroundPid -ErrorAction SilentlyContinue
  if($newDialog.Path -eq 'C:\Program Files\Aspire 12.5\x64\SandboxedFileDialog.exe'){$allowedPids+=@($foregroundPid)}else{throw "Aspire lost focus to PID $foregroundPid handle $([AD]::GetForegroundWindow()); action $($a.type) cancelled."}
 }
 switch($a.type) {
  'maximize' {[void][AD]::ShowWindowAsync($hwnd,3)}
  'click' {
   $r=New-Object AD+RECT;[void][AD]::GetWindowRect($hwnd,[ref]$r)
   [void][AD]::SetCursorPos(($r.Left+[int]$a.x),($r.Top+[int]$a.y))
   if($a.shift){[AD]::keybd_event(16,0,0,[UIntPtr]::Zero)}
   if($a.right){[AD]::mouse_event(8,0,0,0,[UIntPtr]::Zero);[AD]::mouse_event(16,0,0,0,[UIntPtr]::Zero)}else{[AD]::mouse_event(2,0,0,0,[UIntPtr]::Zero);[AD]::mouse_event(4,0,0,0,[UIntPtr]::Zero)}
   if($a.double){Start-Sleep -Milliseconds 80;[AD]::mouse_event(2,0,0,0,[UIntPtr]::Zero);[AD]::mouse_event(4,0,0,0,[UIntPtr]::Zero)}
   if($a.shift){[AD]::keybd_event(16,0,2,[UIntPtr]::Zero)}
  }
  'move' {$r=New-Object AD+RECT;[void][AD]::GetWindowRect($hwnd,[ref]$r);[void][AD]::SetCursorPos(($r.Left+[int]$a.x),($r.Top+[int]$a.y))}
  'key' {Key $a.keys}
  'text' {
   $old=[System.Windows.Forms.Clipboard]::GetDataObject()
   [System.Windows.Forms.Clipboard]::SetText([string]$a.text)
   Key 'CTRL+V';Start-Sleep -Milliseconds 200
   if($old){try{[System.Windows.Forms.Clipboard]::SetDataObject($old,$true)}catch{}}
  }
  'set' {
   [uint32]$targetPid=0;$target=[IntPtr]([long]$a.handle)
   [void][AD]::GetWindowThreadProcessId($target,[ref]$targetPid)
   if($allowedPids -notcontains $targetPid){throw 'Target control is outside Aspire.'}
   [void][AD]::SendMessage($target,12,[IntPtr]::Zero,[string]$a.text)
  }
  'field' {
   $target=FindControl ([int]$a.id) 'Edit'
   [void][AD]::SendMessage($target,12,[IntPtr]::Zero,[string]$a.text)
  }
  'press' {
   $target=[IntPtr]([long]$a.handle);[uint32]$tp=0
   [void][AD]::GetWindowThreadProcessId($target,[ref]$tp)
   if($allowedPids -notcontains $tp){throw 'Button is outside Aspire.'}
   [void][AD]::SendMessage($target,245,[IntPtr]::Zero,$null)
  }
  'wait' {Start-Sleep -Milliseconds ([Math]::Min([int]$a.ms,15000))}
  default {throw "Unknown action $($a.type)"}
 }
 Start-Sleep -Milliseconds 200
}
Start-Sleep -Milliseconds 1000
$r=New-Object AD+RECT;[void][AD]::GetWindowRect($hwnd,[ref]$r)
if($r.Left -lt -10000){throw 'Aspire is minimized.'}
$bmp=New-Object System.Drawing.Bitmap(($r.Right-$r.Left),($r.Bottom-$r.Top))
$g=[System.Drawing.Graphics]::FromImage($bmp)
$shot=Join-Path $run ('06_Evidence\'+$cfg.name+'.png')
try{$g.CopyFromScreen($r.Left,$r.Top,0,0,$bmp.Size);$bmp.Save($shot,[System.Drawing.Imaging.ImageFormat]::Png)}finally{$g.Dispose();$bmp.Dispose()}
$script:controls=New-Object System.Collections.Generic.List[object]
$callback=[AD+EnumProc]{param($h,$p)
 if([AD]::IsWindowVisible($h)){
  $s=New-Object Text.StringBuilder 1024;$c=New-Object Text.StringBuilder 256
  [void][AD]::GetWindowText($h,$s,1024);[void][AD]::GetClassName($h,$c,256)
  $b=New-Object AD+RECT;[void][AD]::GetWindowRect($h,[ref]$b)
  $script:controls.Add([PSCustomObject]@{handle=$h.ToInt64();id=[AD]::GetDlgCtrlID($h);class=$c.ToString();text=$s.ToString();bounds=@(($b.Left-$r.Left),($b.Top-$r.Top),($b.Right-$b.Left),($b.Bottom-$b.Top))})
 };return $true
}
[void][AD]::EnumChildWindows($hwnd,$callback,[IntPtr]::Zero)
$active=[AD]::GetForegroundWindow()
if($active -ne $hwnd){[void][AD]::EnumChildWindows($active,$callback,[IntPtr]::Zero)}
$enumTop=[AD+EnumProc]{param($h,$p)
 [uint32]$ownerPid=0;[void][AD]::GetWindowThreadProcessId($h,[ref]$ownerPid)
 if($allowedPids -contains $ownerPid -and $h -ne $hwnd -and [AD]::IsWindowVisible($h)){[void][AD]::EnumChildWindows($h,$callback,[IntPtr]::Zero)}
 return $true
}
[void][AD]::EnumWindows($enumTop,[IntPtr]::Zero)
$state=[PSCustomObject]@{title=$proc.MainWindowTitle;processId=$proc.Id;window=@($r.Left,$r.Top,($r.Right-$r.Left),($r.Bottom-$r.Top));screenshot=$shot;activeHandle=$active.ToInt64();controls=$script:controls}
$state | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $run ('07_Logs\'+$cfg.name+'.json')) -Encoding UTF8
$state | Select-Object title,processId,window,screenshot,activeHandle,@{n='controlCount';e={$_.controls.Count}} | ConvertTo-Json -Depth 6 -Compress
