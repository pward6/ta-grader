# Read each repository path from the file
$text = "Programming`nQ1: `nWritten:`nQ1: `nQ2: `nQ3: `nQ4: `n"


Get-Content repos.txt | ForEach-Object {
    $repoPath = $_
    Write-Output "adding grade.txt to $repoPath..."

    # Navigate to the student's repository
    Set-Location -Path $repoPath
    New-Item -Path ".\grade.txt" -ItemType File
    $text | Out-File -FilePath ".\grade.txt"
}

