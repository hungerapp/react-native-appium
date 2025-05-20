Feature: Item Management in Branch Settings
    As a branch administrator
    I want to manage the item information of the branch
    To provide a better customer experience

    @regression @item_management @navigation_to_item @setting_brand_and_branch
    Scenario: Navigate to Item
        Given I am on the branch settings page
        When I tap on the Item
        Then I should see the item page

    @regression @item_management @item_list_setting @setting_brand_and_branch
    Scenario: Item List Setting
        Given I am on the item page
        When I tap on the Item in the item page
        And I delete all item category
        And I add a new item category to "新商品分類<current_datetime>"
        And I edit the item category to "新商品分類<current_datetime>" to "要被刪除商品分類<current_datetime>"
        And I delete the item category "要被刪除商品分類<current_datetime>"
        And I add a new item category to "商品分類<current_datetime>"
        And I delete all item
        And I add a new item to "商品分類<current_datetime>" "新商品<current_datetime>" "商品介紹<current_datetime>" "100" "10"
        And I copy the item to "商品分類<current_datetime>" "新商品<current_datetime>"
        And I delete the item to "商品分類<current_datetime>" "新商品<current_datetime>"
        And I edit the item to "商品分類<current_datetime>" "新商品<current_datetime>" to "商品<current_datetime>" "商品介紹<current_date>_edit" "200" "20"
        And I tap on the close button in the item list page
        Then I should see the item page

    @regression @item_management @inventory_setting
    Scenario: Inventory Setting
        Given I am on the item page
        And I have an item "商品分類<current_datetime>" "商品<current_datetime>" "商品介紹<current_datetime>" "100" "10"
        When I tap on the Inventory in the item page
        And I reset all inventory
        And I add a new inventory to "商品分類<current_datetime>" "商品<current_datetime>" "<current_datetime>" "100" "10"
        And I set safety stock to "商品分類<current_datetime>" "商品<current_datetime>" "50"
        And I return the inventory to "商品分類<current_datetime>" "商品<current_datetime>" "<current_datetime>" "100"
        And I see the inventory record to "退倉" "商品分類<current_datetime>" "商品<current_datetime>" "100" "10"
        And I see the inventory record to "新增存貨" "商品分類<current_datetime>" "商品<current_datetime>" "100" "10"
        And I tap on the close button in the inventory page
        And I tap on the back button in the item page
        Then I should see the Branch Settings page


