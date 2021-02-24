#### Website Navigation
`tests/tests_run/website_navigation_test.py`

<br />**TC01 - Verify The Logo Is Clickable**
<br />`test3_logo_is_clickable`

Steps:

1. Open the browser and enter the URL
2. Click WOMEN from the top menu
3. Click the Logo

Expected Result:

1. The site is accessible
2. User is redirected to the category page for Woman
3. User is taken back to the home page

<br />**TC02 - Add To Cart A Product From The Home Page**
<br />`test4_display_product_on_hover`

Steps:
1. Open the browser and enter the URL.
2. Scroll to the Popular section.
3. Move the cursor over the image of the first product
4. Click the "Add to cart" button.

Expected Result:

1. The site is accessible.
2. The Popular section visible.
3. The product's image will change to show either the second image containing the price, product name and three buttons: "Quick view," "Add to cart," and "More."
4. The popup "Product successfully added to your shopping cart" displays, with the image on the left. 
Next to the image, there are: 
    * the product name, the same as in the previous step,
    * "Quantity" = 1, 
    * "Total" with the value equal to the product price.

    The right section of the popup is titled: "There is 1 item in your cart," and there are two buttons: "Continue shopping" and "Proceed to checkout."