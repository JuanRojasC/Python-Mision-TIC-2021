# VARIABLES
examsforVerify, examsRemembered = input().split(" ")
exams = input().split(" ")
examsCopiedTeacher = 0
examsCopied = 0
examsCalificated = []

# EXECUTION
# EXAMS COPIED DETECTED FOR TEACHER
for exam in range(int(examsRemembered), len(exams)):
    for e in range(1,int(examsRemembered)+1):
        if exams[exam] == exams[exam - e] and examsCopiedTeacher < len(exams)-1:
            examsCopiedTeacher += 1

# EXAMS COPIED TOTAL
for exam in range(len(exams)):
    if (exams.count(exams[exam]) > 1) and (exams[exam] not in examsCalificated):
        examsCalificated.append(exams[exam])
        examsCopied += (exams.count(exams[exam]) - 1)


print(examsCopiedTeacher,examsCopied)


# OTHER WAY
# n,k = input().split()
# n, k = int(n), int(k)
# exams = input().split()
# copiedExams = 0
# repeatedExamsTeacher = 0

# repeatedExams = set([i for i in exams if exams.count(i)>1])
# for exam in repeatedExams:
#     copiedExams += exams.count(exam)-1

# for exam in range(k,len(exams)):
#     for i in range(1,k+1):
#         if exams[exam] == exams[exam - i] and repeatedExamsTeacher < len(exams)-1:
#             repeatedExamsTeacher += 1

# print(repeatedExamsTeacher,copiedExams)

