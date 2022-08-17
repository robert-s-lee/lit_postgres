# lit_postgres component

This ⚡ [Lightning component](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init component lit_postgres
```

## To run lit_postgres

First, install lit_postgres (warning: this component has not been officially approved on the lightning gallery):

```bash
lightning install component https://github.com/theUser/lit_postgres
```

Once the app is installed, use it in an app:

```python
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
```
