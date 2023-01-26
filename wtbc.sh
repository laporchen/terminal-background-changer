#!/usr/bin/env bash
imagePath=$WTIMAGEFOLDER
userProfile=$(wslpath "$(wslvar USERPROFILE)")
jsonPath="${userProfile}/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"
jsonContent=$(cat $jsonPath)

if [[ -z $imagePath ]]; then
	echo 'Please add WTIMAGEFOLDER="path to your image folder" to your environment variables'
	exit 0
fi

while true; do
	selected=$(find $imagePath | fzf)
	if [[ -z $selected ]]; then
		exit 0
	fi
	updatePath=$(wslpath -w "$selected")	
	# '.profiles.defaults.backgroundImage = "yo"'
	updatedContent=$(jq '.profiles.defaults.backgroundImage = $path' --arg path "$updatePath" <<< $jsonContent)
	#updatedContent=$(jq '.profiles.defaults.backgroundImage = ${path}' --arg path $updatePath $jsonPath)
	echo $updatedContent > $jsonPath
done
