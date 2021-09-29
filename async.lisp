(defun output (s)
  (format *standard-output* "~a~%" s))

(defun fatalError ()
  (format *standard-output* "FATAL ERROR"))

(defclass component ()
  ((inqueue :accessor inqueue :initform nil)
   (connected-to :accessor connected-to :initarg :connected-to)
   (func :accessor func :initarg :func)))




(defmethod enqueue ((c component) data)
  (setf (inqueue c) (append (inqueue c) (list data))))

(defmethod send ((self component) data)
  (let ((target (connected-to self)))
    (enqueue target data)))

(defmethod empty-queue ((self component))
  (null (inqueue self)))

(defmethod exec-once ((self component))
  (let ((data (pop (inqueue self))))
    (funcall (func self) self data)))

(defclass Dispatcher ()
  ((component-list :accessor component-list :initform nil)))

(defmethod exec ((self Dispatcher))
  (mapc #'(lambda (cmponent)
             (unless (empty-queue cmponent)
               (exec-once cmponent)))
         (component-list self)))


(defmethod nothing-to-do ((self Dispatcher))
  (every #'empty-queue (component-list self)))
   
(defmethod fC ((self component) x)
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

(defmethod fB ((self component) x) 
  (cond ((string= x "q")
         (send self "s"))
        ((string= x "r")
         (send self "t"))
        (t
         (fatalError))))

(defun make-B (target) 
  (let ((self (make-instance 'component :connected-to target :func 'fB)))
    self))

(defun make-C () 
  (let ((self (make-instance 'component :func 'fC)))
    self))

(defmethod initialize ((self Dispatcher))
  (let ((Component2 (make-C)))
    (let ((Component1 (make-B Component2)))
      (let ((clist (list Component1 Component2)))
        (setf (component-list self) clist)
        clist)))) ;; return the list of components

(defun async1 ()
  (let ((dsptchr (make-instance 'Dispatcher)))
    (let ((component-list (initialize dsptchr)))
      (enqueue (first component-list) "q")
      (enqueue (second component-list) "q")
      (loop 
       until (nothing-to-do dsptchr)
       do    (exec dsptchr)))))

(defun async2 ()
  (let ((dsptchr (make-instance 'Dispatcher)))
    (let ((component-list (initialize dsptchr)))
      (enqueue (second component-list) "q")
      (enqueue (first component-list) "q")
      (loop 
       until (nothing-to-do dsptchr)
       do    (exec dsptchr)))))
