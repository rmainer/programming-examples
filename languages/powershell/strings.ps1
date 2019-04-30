# concat
$buf1 = "Hallo";
$buf2 = "Welt";
Write-Output "Hallo $($buf2)";
Write-Output ("{0} {1}" -f $buf1, $buf2)
Write-Host "Hallo" $buf2