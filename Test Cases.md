#### Website Navigation
`tests/tests_run/website_navigation_test.py`

#####URL: http://automationpractice.com/index.php

<br />**TC-NAV01 - Home Page Content Visible**
<br />`test1_home_page_content_visible`

Steps:
1. Open the browser and enter the URL

Expected Results:
1. The site is accessible


<br />**TC-NAV02 - Category Page For Woman Visible**
<br />`test2_category_page_for_woman_visible`

Steps:
1. Open the browser and enter the URL
2. Select WOMEN from the top menu, beneath Your Logo

Expected Results:
1. The site is accessible
2. The user is redirected to the category page for Woman.
The banner titled "Woman" is visible.


<br />**TC-NAV03 - Verify The Logo Is Clickable**
<br />`test3_logo_is_clickable`

Steps:
1. Open the browser and enter the URL
2. Click WOMEN from the top menu, beneath Your Logo
3. Click Your Logo

Expected Results:
1. The site is accessible
2. The user is redirected to the category page for Woman.
The banner titled "Woman" is visible.
3. User is taken back to the home page


<br />**TC-NAV04 - Display Product On Hover**
<br />`test4_display_product_on_hover`

Steps:
1. Open the browser and enter the URL.
2. Scroll to the Popular section.
3. Move the cursor over the image of the first product

Expected Results:
1. The site is accessible.
2. The Popular section visible.
3. The product's image will change to show either the second image containing the price, product name, and three buttons: "Quick view," "Add to cart," and "More."


<br />**TC-NAV05 - Add To Cart A Product From The Home Page**
<br />`test5_popup_title_product_successfully_added_visible`

Steps:
1. Open the browser and enter the URL.
2. Scroll to the Popular section.
3. Move the cursor over the image of the first product
4. Click the "Add to cart" button.

Expected Results:
1. The site is accessible.
2. The Popular section visible.
3. The product's image will change to show either the second image containing the price, product name and three buttons: "Quick view," "Add to cart," and "More."
4. The popup "Product successfully added to your shopping cart" displays, with the image on the left. 
Next to the image, there are: 
<br /> a) the product name corresponding with the name from the previous step,
<br /> b) "Quantity" equal to 1, 
<br /> c) "Total" matching the product price shown previously.
<br /> The right section of the popup is titled: "There is 1 item in your cart."


