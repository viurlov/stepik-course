# stepik-course

Данный репозиторий содержит домашнее задание по курсу:
[Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/)
====
Получить содержимое репозитория можно командой

```
$ git clone https://github.com/viurlov/stepik-course.git
```

====

Параметризованный тест по заданию [3.6 PyTest - параметризация, конфигурирование, плагины, шаг 9](https://stepik.org/lesson/237240/step/9)
содержится в папке unit3_parameterizedTest.

Для запуска теста необходимо выполнить следующие команды:

```
$ git clone https://github.com/viurlov/stepik-course.git
$ cd stepik-course
$ cd unit3_parameterizedTest
$ pytest
```

Запуск pytest без параметров осуществляет запуск тестов в браузере chrome для языка ru
Для запуска тестов с другим языком необходимо выполнить pytest со следующим параметром:

```
$ pytest --language=es 
```

Для запуска с другим языком и браузером необходимо выполнить pytest со следующими параметрами:

```
$ pytest --language=fr --browser=firefox
```
