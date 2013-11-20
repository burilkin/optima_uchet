/* ========================================
========== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ==========
======================================== */

var cookieValuesOfSidebarMenus = [],      // Массив значений кук для каждого меню, где индекс массива - id меню
    $sidebarMenus = [];                   // Массив всех меню сайдбара

/* ===================================
========== ОСНОВНЫЕ ФУНКЦИИ ==========
=================================== */

/* ########## Sidebar hide/show functions ######### */

// Скрыть/показать сайдбар (событие, вызвавшее функцию: клик/загрузка страницы)
function hideShowSidebar(e) {
  /* Установка кук (пример)
  $.cookie("the_cookie", "true", {
	  expires: 7,
	  path: "/",
    domain: "jquery.com",
    secure: true
  });
  */

  /*
    e: event("click"/"load")
    cookie: sidebarShowed (0/1)
  */

  var $sidebar = $("#sidebar"),
      $sidebarInner = $("#sidebarInner"),
      $workArea = $("#workArea"),
      $hideShowBtn = $("#hideShowSidebarBtn"),
      $workAreaMainMenu = $("#workAreaMainMenu"),
      $sidebarShowed = $.cookie("sidebarShowed");

  // Первичная загрузка страницы
  if (e == "load") {
    // Если в куках "скрыт", то скрыть
    if ($sidebarShowed == 0) {
      $sidebar.css("width", hiddenSidebarWidth);
      $sidebarInner.css("display", "none");
      $workArea.css("margin-left", hiddenSidebarWidth);
      $workAreaMainMenu.css("left", hiddenSidebarWidth);
      $workAreaMainMenu.css("width", workAreaMainMenuWidth_SidebarHidden);
      $hideShowBtn.text(hideShowBtn_Show);
      $hideShowBtn.attr("title", hideShowBtn_Show);
    }
  }

  // Нажатие на кнопку "Скрыть/Раскрыть"
  if (e == "click") {
    // Если в куках "скрыт", то раскрыть и записать в куки
    if ($sidebarShowed == 0) {
      $sidebar.css("width", sidebarWidth);
      $sidebarInner.css("display", "block");
      $workArea.css("margin-left", sidebarWidth);
      $workAreaMainMenu.css("left", sidebarWidth);
      $workAreaMainMenu.css("width", workAreaMainMenuWidth_SidebarShowed);
      $hideShowBtn.text(hideShowBtn_Hide);
      $hideShowBtn.attr("title", hideShowBtn_Hide);
      $.cookie("sidebarShowed", 1);
    }
    // Иначе скрыть и записать в куки
    else {
      $sidebar.css("width", hiddenSidebarWidth);
      $sidebarInner.css("display", "none");
      $workArea.css("margin-left", hiddenSidebarWidth);
      $workAreaMainMenu.css("left", hiddenSidebarWidth);
      $workAreaMainMenu.css("width", workAreaMainMenuWidth_SidebarHidden);
      $hideShowBtn.text(hideShowBtn_Show);
      $hideShowBtn.attr("title", hideShowBtn_Show);
      $.cookie("sidebarShowed", 0);
    }
  }
}

// Создать массив соответсвия id меню значеням кук
// Идексы массива - id элементов ul в сайдбаре,
// значения элементов массива - 0/1 (скрыто/раскрыто меню)
function generatecookieValuesOfSidebarMenusWithCookieValue(cookie) {
  var result = [],
      i;

  $sidebarMenus = $("#sidebarInner ul");

  // id каждого меню установить в соответствие значение кук
  for (i = 0; i < $sidebarMenus.length; i++) {
    result[$($sidebarMenus[i]).attr("id")] = cookie[i];
  }

// Вернуть массив кук
return result;
}

// Скрыть/показать меню (кнопка вызова функции)
function hideShowSidebarMenu(sender) {
  var $menu = $(sender).parent(),  // Список, внутри которого находится кнопка
      newCookie = [],
      i;

  if (cookieValuesOfSidebarMenus[$menu.attr("id")] == 0) {
    $menu.children("li").css("display", "block");      // Показать все элементы списка <li>
    cookieValuesOfSidebarMenus[$menu.attr("id")] = 1;  // Добавить изменения состояния в куки
  }
  else {
    $menu.children("li").css("display", "none");       // Скрыть все элементы списка <li>
    cookieValuesOfSidebarMenus[$menu.attr("id")] = 0;  // Добавить изменения состояния в куки
  }

  for (i = 0; i < $sidebarMenus.length; i++) {
    newCookie[i] = cookieValuesOfSidebarMenus[$($sidebarMenus[i]).attr("id")];
  }

  $.cookie("sidebarMenusShowed", newCookie.join(','));
}


/* ########## Work area main menu ########## */

// Скрыть/показать главное меню рабочей зоны (видимость меню зависит от классов "hidden"/"showed"
function hideShowWorkAreaMainMenu()
{
  var $workAreaMainMenu = $("#workAreaMainMenu"),                     // Главное меню рабочей зоны
      $workAreaMainMenuTitle = $($("#workAreaMainMenu .title")[0]),      // Заголовок главного меню рабочей зоны
      $workAreaMainMenuContent = $($("#workAreaMainMenu .content")[0]);  // Содержимое главного меню рабочей зоны

  if ($workAreaMainMenu.hasClass("hidden")) {          // Если меню скрыто, то показать
    $workAreaMainMenu.removeClass("hidden");
    $workAreaMainMenu.addClass("showed");
    $workAreaMainMenuContent.css("display", "block");
    $workAreaMainMenuTitle.attr("title", workAreaMainMenuTitle_Showed);
  }
  else if ($workAreaMainMenu.hasClass("showed")) {     // Иначе, если раскрыто, то скрыть
    $workAreaMainMenu.removeClass("showed");
    $workAreaMainMenu.addClass("hidden");
    $workAreaMainMenuContent.css("display", "none");
    $workAreaMainMenuTitle.attr("title", workAreaMainMenuTitle_Hidden);
  }
}


/*===========================================
========== ПОСЛЕ ЗАГРУЗКИ СТРАНИЦЫ ==========
===========================================*/

$(document).ready(function() {
  var i;
// При первом посещении сайта установить куки (сайдбар раскрыт),
// но если куки уже записаны, то обработать их (т.е. состояние сайдбара установить из кук)
  if ($.cookie("sidebarShowed") == null) {
    $.cookie("sidebarShowed", 1);
  }
  else {
    hideShowSidebar("load");
  }

// Если куки не установлены или количество списков изменилось, то записать куки для каждого списка = 1,
// иначе обработать их (т.е. состояние меню установить из кук)
  $sidebarMenus = $("#sidebarInner ul");
  if (($.cookie("sidebarMenusShowed") == null) || ((($.cookie("sidebarMenusShowed").split(',')).length != $sidebarMenus.length))) {
    var cookieValue = [];

    for (i = 0; i < $sidebarMenus.length; i++) {
      cookieValue[i] = 1;
    }

    $.cookie("sidebarMenusShowed", cookieValue.join(','));  // Записать куки по умолчанию (все меню раскрыты)
    cookieValuesOfSidebarMenus = generatecookieValuesOfSidebarMenusWithCookieValue(cookieValue);  // Создать из кук "Массив значений кук для каждого меню (где индекс = id меню)"
  }
  else {
    // Создать из кук "Массив значений кук для каждого меню (где индекс = id меню)"
    cookieValuesOfSidebarMenus = generatecookieValuesOfSidebarMenusWithCookieValue(($.cookie("sidebarMenusShowed")).split(','));
    // Описать загрузку состояния меню из кук
    // Перебор значений кук для каждого списка
    for (i = 0; i < $sidebarMenus.length; i++) {
      // Если значение кук для текущего списка == 0, то скрыть его элементы
      if (cookieValuesOfSidebarMenus[$($sidebarMenus[i]).attr("id")] == 0) {
        $($sidebarMenus[i]).children("li").css("display", "none");
      }
    }
  }
});