chmod a+w .git -R
git config --local user.name docker
git config --local user.email docker@cloud
git config --local credential.helper "store --file /usr/local/fundhelper-data/gitpass"
echo "https://xxxx%40gmail.com:yyyy@github.com" >> gitpass

