# vimtutor summary

## 1. Moving the cursor, exiting vim, basic text editing, editing file

1. The cursor is moved using either the arrow keys or the hjkl keys.
         h (left)       j (down)       k (up)       l (right)

2. To start Vim from the shell prompt type:  vim FILENAME <ENTER>

3. To exit Vim type:     <ESC>   :q!   <ENTER>  to trash all changes.

           OR type:      <ESC>   :wq   <ENTER>  to save the changes.

4. To delete the character at the cursor type:  x

5. To insert or append text type:

         i   type inserted text   <ESC>         insert before the cursor

         A   type appended text   <ESC>         append after the line

## 2. deletion command, moving cursor using a count for a motion

  1. To delete from the cursor up to the next word type:        `dw`
  2. To delete from the cursor up to the end of the word type:  `de`
  3. To delete from the cursor to the end of a line type:       `d$`
  4. To delete a whole line type:                               `dd`

  5. To repeat a motion prepend it with a number:   `[num][motion]`
  6. The format for a change command is:

               `operator   [number]   motion`

     where:

       operator - is what to do, such as  d  for delete

       [number] - is an optional count to repeat the motion

       motion   - moves over the text to operate on, such as  `w (word)`,

                  `e (end of word)`,  `$ (end of the line)`, etc.

  7. To move to the start of the line use a zero:  `0``

  8. To undo previous actions, type:           `u`  (lowercase u)

     To undo all the changes on a line, type:  `U`  (capital U)

     To undo the undos, type:                  `CTRL-R`

