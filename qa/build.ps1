# Build script to generate a new zip archive to upload to the Google Chrome Web Store.

# Name for the archive to generate.
$archiveName = "df-test-extension"

# Folder where the extension files are located.
$extensionFolder = "df-test-extension"

# Extract the version from the manifest file
$version = (Get-Content -Path .\${extensionFolder}\manifest.json | ConvertFrom-Json).version

# Generate a filename for the zip archive
$filename = "${archiveName}-${version}.zip"

# Create a temporary folder to hold the files to be zipped
$tempFolder = "temp-${archiveName}"
New-Item -ItemType Directory -Path $tempFolder > $null

# Copy the extension files to the temporary folder, excluding the `images` subdirectory
Copy-Item -Path .\${extensionFolder}\* -Destination $tempFolder -Recurse -Exclude "images" > $null

# When publishing to the Chrome Web Store, we must remove localhost and loopback URLs 
# from the manifest JSON file's content_scripts section, as local ports are not allowed.
# Read in $tempFolder\manifest.json, convert it to a PowerShell object, and remove the 
# localhost and loopback URLs from content_type.matches: "*://localhost:*/*" and "*://127.0.0.1:*/*"
$manifestPath = ".\${tempFolder}\manifest.json"
$manifest = Get-Content -Path $manifestPath | ConvertFrom-Json
$manifest.content_scripts[0].matches = $manifest.content_scripts[0].matches | Where-Object { $_ -notlike "*://localhost:*/*" -and $_ -notlike "*://127.0.0.1:*/*" }
$manifest | ConvertTo-Json -Depth 10 | Set-Content -Path $manifestPath

# Write the updated manifest in $manifest to the $tempFolder\manifest.json file
$manifest | ConvertTo-Json -Depth 10 | Set-Content -Path $manifestPath


# Print the contents of the manifest file from the $tempFolder to verify the changes
Write-Host "Updated manifest.json:"
Get-Content -Path $tempFolder\manifest.json

# If a zip file with the same name already exists, remove it
if (Test-Path .\$filename) {
    Remove-Item -Force .\$filename
}

# Create the zip archive from the temporary folder
Compress-Archive -Path .\${tempFolder}\* -DestinationPath .\$filename -CompressionLevel Optimal

# Remove the temporary folder
Remove-Item -Recurse -Force -Path $tempFolder

# Verify the archive was created and is readable
$fullPath = (Resolve-Path .\$filename).Path
if (Test-Path $fullPath) {
    Write-Host "Created zip archive: ${filename}:"
    # Read the contents of the archive
    $zip = [System.IO.Compression.ZipFile]::OpenRead($fullPath)
    $zip.Entries | ForEach-Object {
        Write-Host $_.FullName
    }
    $zip.Dispose()
} else {
    Write-Host "Failed to create archive: ${filename}"
}