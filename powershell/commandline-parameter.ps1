Param (
    [Parameter(Mandatory=$true)]
		[string]$cmd1
		,
		[Parameter(Mandatory=$false)]
		[string]$cmd2
)

Write-Output $cmd1 $cmd2