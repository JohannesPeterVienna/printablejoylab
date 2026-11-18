"""Paper size reference – one data source for the table on /paper-sizes.html and the print scale calculator.

Every row is a self-describing media name from PWG 5101.1 (Printer Working Group, "PWG Media Standardized Names"):
tables 3–6 of the 2013 edition (v2.0) were read in full on 2026-11-18, and each name was then matched letter for letter
against the text of the current 2023 edition (v2.1), which the page cites. Width and height are parsed from the name.
"css" is the page-size keyword from W3C CSS Paged Media Module Level 3 (Working Draft, 14 September 2023), if one exists.
"""
import math, re

GROUPS = [("iso-a", "ISO A series"), ("iso-b", "ISO B series"), ("iso-c", "ISO C series and DL (envelopes)"), ("na", "North American sheets"),
          ("na-large", "US engineering and architectural sheets"), ("jis", "Japanese sizes (JIS B, Hagaki)"), ("press", "ISO RA and SRA (untrimmed press sheets)")]

_ROWS = [
    *[(f"A{i}", "iso-a", n) for i, n in enumerate("iso_a0_841x1189mm iso_a1_594x841mm iso_a2_420x594mm iso_a3_297x420mm iso_a4_210x297mm iso_a5_148x210mm iso_a6_105x148mm iso_a7_74x105mm iso_a8_52x74mm iso_a9_37x52mm iso_a10_26x37mm".split())],
    *[(f"B{i}", "iso-b", n) for i, n in enumerate("iso_b0_1000x1414mm iso_b1_707x1000mm iso_b2_500x707mm iso_b3_353x500mm iso_b4_250x353mm iso_b5_176x250mm iso_b6_125x176mm iso_b7_88x125mm iso_b8_62x88mm iso_b9_44x62mm iso_b10_31x44mm".split())],
    *[(f"C{i}", "iso-c", n) for i, n in enumerate("iso_c0_917x1297mm iso_c1_648x917mm iso_c2_458x648mm iso_c3_324x458mm iso_c4_229x324mm iso_c5_162x229mm iso_c6_114x162mm iso_c7_81x114mm iso_c8_57x81mm iso_c9_40x57mm iso_c10_28x40mm".split())],
    ("DL envelope", "iso-c", "iso_dl_110x220mm"),
    ("US Letter", "na", "na_letter_8.5x11in"), ("US Legal", "na", "na_legal_8.5x14in"), ("Ledger / Tabloid", "na", "na_ledger_11x17in"),
    ("Half Letter (Statement)", "na", "na_invoice_5.5x8.5in"), ("US Executive", "na", "na_executive_7.25x10.5in"),
    ("Government Letter", "na", "na_govt-letter_8x10in"), ("Government Legal", "na", "na_govt-legal_8x13in"),
    ("Foolscap", "na", "na_foolscap_8.5x13in"), ("Oficio (Mexico)", "na", "na_oficio_8.5x13.4in"), ("Quarto", "na", "na_quarto_8.5x10.83in"),
    ("Index card 3 × 5", "na", "na_index-3x5_3x5in"), ("Index card 4 × 6", "na", "na_index-4x6_4x6in"), ("5 × 7", "na", "na_5x7_5x7in"),
    ("Index card 5 × 8", "na", "na_index-5x8_5x8in"), ("#10 envelope", "na", "na_number-10_4.125x9.5in"), ("Monarch envelope", "na", "na_monarch_3.875x7.5in"),
    ("Super B (13 × 19)", "na", "na_super-b_13x19in"),
    ("Engineering C", "na-large", "na_c_17x22in"), ("Engineering D", "na-large", "na_d_22x34in"), ("Engineering E", "na-large", "na_e_34x44in"),
    ("Arch A", "na-large", "na_arch-a_9x12in"), ("Arch B", "na-large", "na_arch-b_12x18in"), ("Arch C", "na-large", "na_arch-c_18x24in"),
    ("Arch D", "na-large", "na_arch-d_24x36in"), ("Arch E", "na-large", "na_arch-e_36x48in"),
    *[(f"JIS B{i}", "jis", n) for i, n in enumerate("jis_b0_1030x1456mm jis_b1_728x1030mm jis_b2_515x728mm jis_b3_364x515mm jis_b4_257x364mm jis_b5_182x257mm jis_b6_128x182mm jis_b7_91x128mm jis_b8_64x91mm jis_b9_45x64mm jis_b10_32x45mm".split())],
    ("Hagaki (postcard)", "jis", "jpn_hagaki_100x148mm"),
    *[(f"RA{i}", "press", n) for i, n in enumerate("iso_ra0_860x1220mm iso_ra1_610x860mm iso_ra2_430x610mm iso_ra3_305x430mm iso_ra4_215x305mm".split())],
    *[(f"SRA{i}", "press", n) for i, n in enumerate("iso_sra0_900x1280mm iso_sra1_640x900mm iso_sra2_450x640mm iso_sra3_320x450mm iso_sra4_225x320mm".split())],
]
CSS = {"iso_a5_148x210mm": "A5", "iso_a4_210x297mm": "A4", "iso_a3_297x420mm": "A3", "iso_b5_176x250mm": "B5", "iso_b4_250x353mm": "B4",
       "jis_b5_182x257mm": "JIS-B5", "jis_b4_257x364mm": "JIS-B4", "na_letter_8.5x11in": "letter", "na_legal_8.5x14in": "legal", "na_ledger_11x17in": "ledger"}
OURS = {"iso_a4_210x297mm": "a4", "na_letter_8.5x11in": "letter", "iso_a5_148x210mm": "a5", "na_invoice_5.5x8.5in": "half"}   # sizes our generators offer


def _num(x, digits):
    s = f"{x:.{digits}f}"
    return s.rstrip("0").rstrip(".") if "." in s else s


def rows():
    out = []
    for label, group, pwg in _ROWS:
        m = re.fullmatch(r"[a-z]+_[a-z0-9-]+_([\d.]+)x([\d.]+)(mm|in)", pwg)
        assert m, pwg
        w, h, unit = float(m[1]), float(m[2]), m[3]
        k = 25.4 if unit == "in" else 1.0
        wmm, hmm = w * k, h * k
        out.append({"label": label, "group": group, "pwg": pwg, "unit": unit, "wmm": round(wmm, 3), "hmm": round(hmm, 3),
                    "mm": f"{_num(wmm, 1)} × {_num(hmm, 1)}", "inch": f"{_num(wmm / 25.4, 2)} × {_num(hmm / 25.4, 2)}",
                    "pt": f"{_num(wmm / 25.4 * 72, 1)} × {_num(hmm / 25.4 * 72, 1)}", "ratio": f"1 : {hmm / wmm:.3f}",
                    "css": CSS.get(pwg, ""), "ours": OURS.get(pwg, "")})
    return out


def check():
    """Build-time checks behind the statements on the page. Returns the numbers quoted there."""
    r = {x["label"]: x for x in rows()}
    assert len({x["pwg"] for x in r.values()}) == len(_ROWS) == len(r)
    for prefix, last in (("A", 10), ("B", 10), ("C", 10), ("JIS B", 10), ("RA", 4), ("SRA", 4)):
        for i in range(last):
            big, small = r[f"{prefix}{i}"], r[f"{prefix}{i + 1}"]
            assert (small["wmm"], small["hmm"]) == (math.floor(big["hmm"] / 2), big["wmm"]), (prefix, i)   # halved across the long side, rounded down
    for i in range(11):   # C lies between A and B: within 1 mm of the geometric mean of the two
        a, b, c = r[f"A{i}"], r[f"B{i}"], r[f"C{i}"]
        assert abs(math.sqrt(a["wmm"] * b["wmm"]) - c["wmm"]) < 1 and abs(math.sqrt(a["hmm"] * b["hmm"]) - c["hmm"]) < 1, i
    a0 = r["A0"]
    worst = max(abs(x["hmm"] / x["wmm"] - math.sqrt(2)) for x in r.values() if x["group"] in ("iso-a", "iso-b") and x["wmm"] >= 105)
    assert worst < 0.01
    return {"a0_area": a0["wmm"] * a0["hmm"] / 1e6, "count": len(r), "ratio_dev": worst}
