# 0x04. Loops, conditions and parsing

## Description
This Holberton School project is about shell loops, conditions, and parsing. Most importantly, I learnt how to create `SSH keys`. How to use `while`, `until` and `for` loops. How to use `if`, `else`, `elif`, and `case` condition statements. How to use `cut` command, and files and other comparison operators.

## More info

**Shellcheck**
[`Shellcheck`](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task.

## Table of contents
Files | Desciption
----- | ----------
[0. Create a SSH RSA key pair](./0-RSA_public_key.pub) | Create a RSA key pair.
[1. For Best School loop](./1-for_best_school) | Bash script that displays `Best School` 10 times.
[2. While Best School loop](./2-while_best_school) | Bash script that displays `Best School` 10 times.
[3. Until Best School loop](./3-until_best_school) | Bash script that displays `Best School` 10 times.
[4. If 9, say Hi!](./4-if_9_say_hi) | Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.
[5. 4 bad luck, 8 is your chance](./5-4_bad_luck_8_is_your_chance) | Bash script that loops from 1 to 10 and: displays `bad luck` for the 4th loop iteration. displays `good luck` for the 8th loop iteration displays `Best School` for the other iterations
[6. Superstitious numbers](./6-superstitious_numbers) | Bash script that displays numbers from 1 to 20 and: displays `4` and then `bad luck from China` for the 4th loop iteration. displays `9` and then `bad luck from Japan` for the 9th loop iteration. displays `17` and then `bad luck from Italy` for the 17th loop iteration
[7. Clock](./7-clock) | Bash script that displays the time for 12 hours and 59 minutes: display hours from 0 to 12. display minutes from 1 to 59
[8. For ls](./8-for_ls) | Bash script that displays: The content of the current directory. In a list format. Where only the part of the name after the first dash is displayed (refer to the example)
[9. To file, or not to file](./9-to_file_or_not_to_file) | Bash script that gives you information about the `school` file.
[10. FizzBuzz](./10-fizzbuzz) | Bash script that displays numbers from 1 to 100.
[11. Read and cut](./100-read_and_cut) | Bash script that displays the content of the file `/etc/passwd`.
[12. Tell the story of passwd](./101-tell_the_story_of_passwd) | Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.
[13. Let's parse Apache logs](./102-lets_parse_apache_logs) |  Bash script that displays the visitor IP along with the [`HTTP status code`](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) from the Apache log file.
[14. Dig the data](./103-dig_the-data) | Bash script that groups visitors by IP and HTTP status code, and displays this data.
