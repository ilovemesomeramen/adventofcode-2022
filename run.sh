
while getopts d:p:i: flag
do
    case "${flag}" in
        d) day=${OPTARG};;
        p) part=${OPTARG};;
        i) input=${OPTARG};;
        *) echo "Invalid option";;
    esac
done

runs=()

echo "Running day $day part $part"
if [ -z ${input+x} ]; then
  echo "No input file specified, using default"
else
  input=" $(realpath "$input")"
  echo "Using input file $input"
fi
echo ""
cd "./day$day" || exit
echo "Changed directory to $(pwd)"

for lang_f in */; do
  runs+=("${lang_f}day$day-part$part"*)
done


run_command="hyperfine -N --warmup 3 --export-markdown ./results.md"
args=()
for val in "${runs[@]}"; do
  args+=("$val$input")
done
echo "Running command:"
echo -e "$run_command" "${args[@]}" "\n"
$run_command "${args[@]}"

cd ../