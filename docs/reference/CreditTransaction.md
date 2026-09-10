# CreditTransaction

A single credit ledger entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the credit transaction | 
**type** | **str** | Credit category. &#x60;ai&#x60; covers every AI-powered feature. | 
**feature** | **str** | Which product the credits relate to. Set on deductions and on the credits a refund returns, absent on credit-pack top-ups, which are not tied to a single feature.  | [optional] 
**amount** | **int** | How many credits this entry moved, signed: positive for top-ups (&#x60;+30&#x60; from a credit pack), negative for deductions (&#x60;-2&#x60; for a two-page import). Sum only entries whose &#x60;state&#x60; is &#x60;active&#x60;.  | 
**source** | **str** | Which pool the credits came from:  * &#x60;subscription&#x60;: the plan&#39;s periodic allowance * &#x60;purchase&#x60;: credits bought as a pack, which do not expire with the billing period * &#x60;free_tier&#x60;: promotional grants * &#x60;support&#x60;: a manual adjustment made by Flat&#39;s support team  A single import can produce two entries when it spans two pools: the plan allowance is drawn down first, and the remainder comes from &#x60;purchase&#x60;.  | 
**state** | **str** | Whether the entry still counts:  * &#x60;active&#x60;: in effect * &#x60;canceled&#x60;: reversed, and no longer affecting the balance. Deductions are   canceled when the import they paid for fails or is refunded.  | 
**job** | **str** | Identifier of the import this entry belongs to, when it relates to one.  Present on an import&#39;s deduction, on its reversal, and on credits returned when an import is refunded. Absent on credit-pack top-ups and manual adjustments.  | [optional] 
**creation_date** | **datetime** | When the transaction was created | 
**modification_date** | **datetime** | When the transaction was last modified | 

## Example

```python
from flat_api.models.credit_transaction import CreditTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTransaction from a JSON string
credit_transaction_instance = CreditTransaction.from_json(json)
# print the JSON string representation of the object
print(CreditTransaction.to_json())

# convert the object into a dict
credit_transaction_dict = credit_transaction_instance.to_dict()
# create an instance of CreditTransaction from a dict
credit_transaction_from_dict = CreditTransaction.from_dict(credit_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


