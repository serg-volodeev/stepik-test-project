# Тестовый проект
Это финальный тестовый проект по курсу [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)

В проекте использовался паттерн Page Object.

**Page Object Model** или кратко Page Object — это паттерн программирования, который очень популярен в автоматизации тестирования и является одним из стандартов при автоматизации тестирования веб-продуктов. Это также один из удобных способов структурировать свой код таким образом, чтобы его было удобно поддерживать, менять и работать с ним.

Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса. Способы взаимодействия пользователя со страницей можно описать с помощью методов класса. В идеале тест, который будет использовать Page Object, должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия с браузером и страницей. При изменениях в верстке страницы не придется исправлять тесты, связанные с этой страницей. Вместо этого нужно будет поправить только класс, описывающий страницу.

Реализовано несколько тест-кейсов для главной страницы интернет-магазина и страницы товара.