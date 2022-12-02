
while getopts d:p: flag
do
    case "${flag}" in
        d) day=${OPTARG};;
        p) part=${OPTARG};;
        *) echo "Invalid option";;
    esac
done

runs=()

echo "Running day $day part $part"

cd "./day$day" || exit

for lang_f in */; do
  runs+=("${lang_f}day$day-part$part"*)
done

run_command="hyperfine -N --warmup 3 --export-markdown ./results.md"
for val in "${runs[@]}"; do
  run_command="$run_command '$val'"
done
echo "$run_command"
$run_command

cd ../