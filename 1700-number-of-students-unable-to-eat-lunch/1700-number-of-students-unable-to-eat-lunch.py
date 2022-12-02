class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Iterate through the stack & queue together
        count = 0
        while count != len(students):
            stu, san = students[0], sandwiches[0]
            if stu == san:
                students.pop(0)
                sandwiches.pop(0)
                count = 0 # reset
            else:
                front = students.pop(0)
                students.append(front)
                count += 1

        return len(students)