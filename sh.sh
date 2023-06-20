#!/bin/bash
find -name '*.mp3' -print0 | xargs -0 md5sum | sort | uniq -Dw 32

declare -A arr
shopt -s globstar

for file in **; do
  [[ -f "$file" ]] || continue
   
  read cksm _ < <(md5sum "$file")
  if ((arr[$cksm]++)); then 
    echo "rm $file"
  fi
done
