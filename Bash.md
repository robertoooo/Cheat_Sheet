### Checks

The flag f checks that the provided path exists and is a regular file
```sh
attempts=10
while [! -f ${path_to_file_variable} ];
do
  if [ "$attempts" == 0]; then
    echo "the provided path does not exists or is not a regular file"
    exit 1
  fi
  ((attempts--)) #reduce one from variable
done
```

The flag -z checks that the variable lenght is zero.
```sh
if [-z "${variable}"]; then
  echo "the variable lenght is zero"
```

