class OwnList(list):
    def pretty_print(self):
        for item in self:
            print(f"🤾 {item}")


own_list = OwnList([1, 2, 3])
own_list.append(4)
own_list.pretty_print()

# OUTPUT
# 🤾 1
# 🤾 2
# 🤾 3
# 🤾 4
