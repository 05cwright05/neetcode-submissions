class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """ 
            Given an array of asteroids

            The index is their position in sapce

            All asteroids move same speed ( negative / positive value) indicates right / left
                - thus can only collide if they have different signs
                - also i.e. [-5, 1] will never colid
                but [,1,1,1,1,1,1,-5] all the ones should die

                same size both die

            
            Inital idea:
                - each positive value we see add it to the top of a stack
                - When a negative comes along pop from the stack if the negative is greater than or equal to
                - if they are the same but still pop and then break

                if our negative stroid survived then he is a giga chad and will not die at all so we can add him to the result
                if he died thats fine he jsut dies



        """
        result = []
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # less than 0
                while len(stack) > 0 and abs(asteroid) > stack[-1]:
                    stack.pop()
                if len(stack) > 0 and abs(asteroid) == stack[-1]:
                    stack.pop()
                else:
                    if len(stack) == 0:
                        result.append(asteroid)

        for value in stack:
            result.append(value)
        return result    
