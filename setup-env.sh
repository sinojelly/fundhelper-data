chmod a+w .git -R
git config --local user.name docker
git config --local user.email docker@cloud
git config --local credential.helper "store --file /usr/local/fundhelper/data/.gitpass"
echo "https://$1%40gmail.com:$2@github.com" >> .gitpass

