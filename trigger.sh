echo "Triggering deployment at $(date)" >> fastAPI/junk_trigger_file.txt
git add fastAPI/junk_trigger_file.txt
git add .
git commit -m "Fix for testing and running container"
git push origin fastAPI
