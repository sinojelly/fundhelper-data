# $1 -- username
# $2 -- pass
# $3 -- path
# $4 -- git cmd

chmod a+w $3/.git -R
$4 config --local user.name docker
$4 config --local user.email docker@cloud
$4 config --local credential.helper "store --file $3/.gitpass"
echo "https://$1%40gmail.com:$2@github.com" > $3/.gitpass

