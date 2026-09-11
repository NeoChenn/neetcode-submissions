class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsQueue = deque(students)
        count = 0

        for sandwich in sandwiches:
            while True:
                student = studentsQueue.popleft()
                if student != sandwich:
                    studentsQueue.append(student)
                    count += 1
                    if count > len(studentsQueue):
                        return len(studentsQueue)
                else:
                    count = 0
                    break

        return 0


