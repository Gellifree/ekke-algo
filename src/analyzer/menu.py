class MenuDrawer:
    @staticmethod
    def draw(elements):
        index = 0
        for element in elements:
            if(element == "Kilépés"):
                print("    [Q] {}".format(element))
            else:
                print("    [{}] {}".format(index, element))
            index += 1
        print()
        answer = input(" >> ")

        try:
            answer = int(answer)
            if(answer >= 0 and answer < len(elements)):
                if(elements[answer] == "Kilépés"):
                    return -1
                return answer
			# normal answer between array indexes including quitting
            else:
                print("Nem megfelelő index.")
                return -2
                # over, or underindexing
        except:
            if(answer == "Q" or answer == "q"):
                return -1
				# exitcode again
            else:
                print("Választás értelmezhetetlen.")
                return -3
				# unidentified command