# win_metrics.ps1 - Grabs Windows performance stats
$cpu = (Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average
$mem = (Get-CimInstance Win32_OperatingSystem | ForEach-Object { ($_.TotalVisibleMemorySize - $_.FreePhysicalMemory) / $_.TotalVisibleMemorySize * 100 })
$disk = (Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" | ForEach-Object { ($_.Size - $_.FreeSpace) / $_.Size * 100 })

Write-Output "cpu:$($cpu),mem:$($mem),disk:$($disk)"
