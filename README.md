# TenzorPythonTestProject

## Тестовое задание на позицию разработчика в тестировании (Программист-тестировщик).
### Правила выполнения задания:
1) Необходимо автоматизировать проверки двух обязательных сценариев.
2) Третий сценарий выполнять не обязательно, но это будет дополнительным плюсом на
техническом собеседовании.
3) Автотесты реализованы на Python 3 и Selenium Webdriver
4) В качестве тестового framework используется pytest
5) Реализован паттерн PageObject
6) Приветствуются любые сторонние библиотеки для логирования, отчетов, selenium
wrapper
7) Готовый проект залит на github/gitlab без кешей, драйверов и виртуальных
окружений. С открытым доступом на чтение.

### Первый сценарий:
1) Перейти на https://sbis.ru/ в раздел "Контакты"
2) Найти баннер Тензор, кликнуть по нему

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img1.png)

3) Перейти на https://tensor.ru/

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img2.png)

4) Проверить, что есть блок "Сила в людях"

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img3.png)

5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
https://tensor.ru/about
6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии
одинаковые высота (height) и ширина (width)

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img4.png)

### Второй сценарий:
1) Перейти на https://sbis.ru/ в раздел "Контакты"
2) Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть
список партнеров.

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img1-1.png)

3) Изменить регион на Камчатский край

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img1-2.png)

4) Проверить, что подставился выбранный регион, список партнеров изменился, url и
title содержат информацию выбранного региона

![image alt](https://github.com/SeleznevSergei/TenzorPythonTestProject/blob/main/img/img1-3.png)
