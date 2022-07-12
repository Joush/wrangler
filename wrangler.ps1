while (1){
  $wsh = New-Object -ComObject WScript.Shell
  write-host ""
  $wsh.SendKeys('+{F15}')
  Start-Sleep -seconds 59
}
