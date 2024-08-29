# RuleBasedPolygonGen
I've developed a method to create unique and interesting polygons by modifying the length of each drawn side according to specific rules. The process continues until a complete shape is formed.

# How it works
Drawing a regular polygon involves creating a series of lines at specific angles. 

https://github.com/user-attachments/assets/16647da6-aabf-4c74-900e-b533ec27d69f

However, by applying certain rules, we can change the length of each side as we draw. For example, we could apply a rule where each 2 sides drawn, the length of the side is multiplied by 2.

https://github.com/user-attachments/assets/8a15fea1-35f3-4369-a11d-dd7fb2cd2230

Or, on every six sides, the length is multiplied by zero, effectively skipping that side.

https://github.com/user-attachments/assets/a7d1d31e-fc0a-408e-b172-72f5d10a8489

This process generate some really cool figures. This code allows user to customize these rules to create the shapes they want.
Additionally, multiple rules can overlap to generate even more complex and fascinating figures. For instance, you could combine the two rules mentioned above: each 2 sides drawn, the length of the side is multiplied by 2 and on every six sides, the length is multiplied by zero.

https://github.com/user-attachments/assets/367852ad-3bdd-4496-be9d-4a8d4d0b525b

Some rules could even involve multiplying the length by -1, which creates even more unique and surprising results.

![Turn,multiplication = (6, -1)](https://github.com/user-attachments/assets/20bf5af6-fe10-4a1b-9cbd-f6057c5aef6a)


