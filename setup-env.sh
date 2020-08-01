# $1 -- username
# $2 -- pass
# $3 -- path

chmod a+w .git -R
git config --local user.name docker
git config --local user.email docker@cloud
git config --local credential.helper "store --file $3/.gitpass"
echo "https://$1%40gmail.com:$2@github.com" > $3/.gitpass

