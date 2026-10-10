from Bio import SeqIO
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def read_fasta(file_name):

    logging.info("Reading FASTA file: %s", file_name)

    try:
        records = list(SeqIO.parse(file_name, "fasta"))

    except FileNotFoundError:
        logging.error("FASTA file not found: %s", file_name)
        return []

    if not records:
        logging.warning("FASTA file contains no sequences.")
        return []

    logging.info("Successfully loaded %d sequences.", len(records))

    return records
