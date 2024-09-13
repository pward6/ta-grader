$commitMessage = "Graded assignments"

# Read each repository path from the file
Get-Content repos.txt | ForEach-Object {
    $repoPath = $_
    Write-Output "Processing $repoPath..."

    # Navigate to the student's repository
    Set-Location -Path $repoPath

    git add .

    git commit -m $commitMessage

    git push origin main 
}
