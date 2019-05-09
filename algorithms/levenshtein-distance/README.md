# Levenshtein distance

Implementations for the *levenshtein distance* in serveral programming languages.

* Bash: `bash levenshtein.sh`
* C: `gcc -Wall -ansi -o levenshtein levenshtein.c`
* C#: `csc /t:exe /out:Levensthein.exe Levenshtein.cs`
* Java: `java Levenshtein.java`
* JavaScript: `node levenshtein.js`
* Lua: `lua levenshtein.lua`
* Pascal: `fpc -olevenshtein levenshtein.pas`
* Perl: `perl levenshtein.pl`
* PHP: `php levenshtein.php`
* PowerShell: `powershell levenshtein.ps1`
* Python: `python levenshtein.py`
* Ruby: `ruby levenshtein.rb`
* Visual Basic: `vbc /t:exe /out:Levenshtein.exe Levenshtein.vb`

Note:

* `csc` and `vbc` are in a subdirectory of `C:\Windows\Microsoft.Net\Framework64`, use the following powershell command to determine the exact directory:

```powershell
Get-ChildItem -Directory $env:SystemRoot\Microsoft.Net\Framework64 | Select -ExpandProperty "Name" | Select-String '^v' | Sort -Descending
```