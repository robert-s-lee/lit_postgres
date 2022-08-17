from lit_postgres import TemplateComponent

import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_postgres = TemplateComponent()

    def run(self):
        print("this is a simple Lightning app to verify your component is working as expected")
        self.lit_postgres.run()


app = L.LightningApp(LitApp())
