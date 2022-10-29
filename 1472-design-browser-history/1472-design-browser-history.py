class BrowserHistory:
    def __init__(self, homepage: str):
        # Create 2 stacks to track the past and future pages
        self.history = [homepage] # add homepage to history
        self.future = []

    def visit(self, url: str) -> None:
        self.history.append(url) # add current_page to history 
        self.future = [] # reset future every time we visit a new page

    def back(self, steps: int) -> str:
        # Loop when we have steps to take & have atleast 1 page in history
        # pay special attention to the homepage (> 1 condition)
        while len(self.history) > 1 and steps > 0:
            self.future.append(self.history.pop()) # add to future
            steps -= 1 # decrement steps

        return self.history[-1] # return the current page

    def forward(self, steps: int) -> str:
        # Loop when we have steps to take & have future pages
        # pay special attention to the > 0 condition
        while self.future and steps > 0:
            self.history.append(self.future.pop()) # add to history
            steps -= 1 # decrement steps

        return self.history[-1] # return the current page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)