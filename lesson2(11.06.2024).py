number_of_completed_tasks = 12  #Количество выполненных ДЗ.
number_of_hours_spent = 1.5  #Количество тзатраченных часов.
course_title = 'Python'  #Название курса.
time_second_task = (number_of_hours_spent / number_of_completed_tasks)  #Время на одно задание.

print(f'Курс: {course_title}, всего задач: {number_of_completed_tasks}, затрачено часов: {number_of_hours_spent}, среднее время выполнения {time_second_task} часа.')  #Вывод переменных в одну строку с использлванием f-строк.