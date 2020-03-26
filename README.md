# classroom
# -*- coding: UTF-8 -*-
def class_scores():
    """
    读取文件为列表，添加总分和平均分
    :return:
    """
    with open(r'E:\work\report.txt','r') as f:
        test=f.readlines()
       # print(test)
    scores = []
    sum_subjects = []
    avg_subjects=[]
    for line in test:
        ls=line.split()
        scores.append(ls)
    #print(scores)
    scores[0].append('总分')
    scores[0].append('平均分')
    #scores.insert(1, avg_subjects)
    #print(scores)

    """
    求学生个人成绩总和和平均分，并以总分排序
    """
    for student_scores in scores[1:]:
        zf = 0
        for subject_scores in student_scores[1:]:
            subject_scores = float(subject_scores)
            zf += subject_scores
        student_scores.append(str(zf))
        student_scores.append('%.2f'%(zf/9))
        #print(student_scores)
    #print(scores)
    scores.sort(key=lambda x:x[10],reverse=True)
    #print(scores)

    """
    求各科成绩平均分，并插入第二列
    """
    i=len(student_scores[1:])
    k=len(scores[1:])
    for subject in range(i):
        sum_subjects.append('0')
        avg_subjects.append('0')
    #sum_subjects.insert(0,'平均')
    #print(len(student_scores[1:]))
    # print(sum_subjects)
    for student_scores in scores[1:]:
        subject_scores=student_scores[1:]
        #print(subject_scores)
        for subject in range(i):
            #print(subject_scores[subject])
            sum_j=float(subject_scores[subject])
            sum_k=float(sum_subjects[subject])
            sum_subjects[subject]=sum_j+sum_k
    for subject in range(i):
        avg_j=float(sum_subjects[subject])
        avg_k='%.2f'%(avg_j/k)
        avg_subjects[subject]=avg_k
    avg_subjects.insert(0, '平均')
    #print(sum_subjects)
    #print(avg_subjects)
    scores.insert(1,avg_subjects)
    #print(scores)
    x=0
    scores[0].insert(0,'序号')
    #print(scores[0])

    """
    低于60分的替换成不及格
    """
    for student_scores in scores[1:]:
        student_scores.insert(0,x)
        x+=1
    #print(scores)
    number=2,3,4,5,6,7,8,9,10
    for student_scores in scores[1:]:
        for subject in number:
            if float(student_scores[subject]) < 60.00:
                student_scores[subject] = '不及格'
    print(scores)

    """
    写入新的txt中
    """
    with open(r'E:\work\result.txt','w') as f1:
        for student_scores in scores:
            for subject_scores in student_scores:
                f1.write(str(subject_scores)+'\t')
            f1.write('\n')
class_scores()
