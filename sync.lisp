(defun output (s)
  (format *standard-output* "~a~%" s))

(defun fatalError ()
  (format *standard-output* "FATAL ERROR"))

(defun C (x)
  (cond ((string= x "q")
         (output "v"))
        ((string= x "r")
         (output "w"))
        ((string= x "s")
         (output "x"))
        ((string= x "t")
         (output "y"))
        ((string= x "u")
         (output "z"))
        (t
         (fatalError))))

(defun B (x) 
  (cond ((string= x "q")
         (C "s"))
        ((string= x "r")
         (C "t"))
        (t
         (fatalError))))


(defun codeV1 ()
  (B "q")
  (C "q"))

(defun codeV2 ()
  (C "q")
  (B "q"))

(defun sync ()
  (format *standard-output* "Version 1~%")
  (codeV1)
  (format *standard-output* "Version 2~%")
  (codeV2))

