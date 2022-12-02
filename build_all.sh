REPO_PATH=$(dirname "$(realpath "$0")")
echo "$REPO_PATH"
mkdir -p /tmp/adventofcode
cmake -S "$REPO_PATH" -B /tmp/adventofcode/
cd /tmp/adventofcode || exit
make -j 9
cd "$REPO_PATH" || exit
