BASH_HANGUL_PATH="."

# code starts HERE

for k in "${!gksdud[@]}"; do
    bind \"$k\":\"${gksdud[$k]}\"
done
