% DCG for sentence: Large crowds listened to the orchestra.
% the man rejected elective surgery.
% An airplane flew over the city


adjective_1 --> [Large].
noun_subject_1 --> [crowds].
verb_1 --> [listened].
pp --> [to].
det_1 --> [the].
noun_object_2  --> [orchestra].
noun_subject_2 --> [man].
verb_2 --> [rejected].
adjective_2 --> [elective].
noun_object_1 --> [surgery].
noun_subject_3 --> [airplane].
det_2 --> [An].
verb_3 --> [flew].
noun_object_3 --> [city].
p --> [over]. 

s --> noun_phrase_subject, vp.
noun_phrase_subject --> adjective_1, noun_subject_1.
noun_phrase_subject --> det_1, noun_subject_2.
noun_phrase_subject --> det_2, noun_subject_3.
vp --> verb_1, noun_object_1.
vp --> verb_2, noun_object_2.
vp --> verb_3, noun_object_3.
noun_object_1 --> pp, noun_phrase.
noun_object_2 --> adjective_2, noun_object_1.
noun_object_3 --> p, np_obj_other.
noun_phrase --> det_1, noun_object_2.
np_obj_other --> det_1, noun_object_3.




