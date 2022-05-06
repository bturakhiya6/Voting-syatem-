#creating voting system
nominee_1=input("enter nominee 1 name:  ") 
nominee_2=input("enter nominee 2 name:  ") 
nominee_3=input("enter nominee 3 name:  ") 

nom_1_vote=0
nom_2_vote=0
nom_3_vote=0

voter_id = [1,2,3,4,5,6,7,8]
num_of_voter = len(voter_id)
 
while True:
    if voter_id==[]:
        print("voting session is over now")
        if nom_1_vote>nom_2_vote and nom_1_vote>nom_3_vote:
           percent=(nom_1_vote/num_of_voter)*100
           print(nominee_1," has won","with",percent,"% votes")
           break
        elif nom_2_vote>nom_1_vote and nom_2_vote>nom_3_vote:
           percent=(nom_2_vote/num_of_voter)*100
           print(nominee_2," has won","with",percent,"% votes")
           break
        elif nom_3_vote>nom_2_vote and nom_3_vote>nom_2_vote:
           percent=(nom_3_vote/num_of_voter)*100
           print(nominee_3," has won","with",percent,"% votes")
           break
    else:

        voter=int(input("enter your voter id no:   "))
        if voter in voter_id:
            print("you are a voter")
            voter_id.remove(voter)
            vote=int(input("enter your vote 1 or 2 or 3 :   "))
            if vote==1:
                nom_1_vote+=1
                print("thank you for casting your vote")
            elif vote==1:
                nom_2_vote+=1
                print("thank you for casting your vote")
            elif vote==1:
                nom_3_vote+=1
                print("thank you for casting your vote")   
        else:
            print("you are not a voter or you have already voted")