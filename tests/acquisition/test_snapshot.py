from meridianforge.acquisition.snapshot import (
    UnderwritingSnapshot,
)


def test_underwriting_snapshot_creation():

    snapshot = UnderwritingSnapshot(
        purchase_price=200000,
        monthly_rent=2000,
        annual_cash_flow=6000,
        cap_rate=0.06,
        cash_on_cash_return=0.10,
        dscr=1.5,
        monthly_cash_flow=500,
    )

    assert snapshot.purchase_price == 200000
    assert snapshot.dscr == 1.5
