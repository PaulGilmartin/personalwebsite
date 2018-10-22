from collections import namedtuple

# TODO: In this function we store some hard-coded data for the publications,
# since I can't currently find a way to upload a record with long text fields to mysql in the prod db
# To find a way to fix this and eliminate need for hard-coded publication data in this static file
PublicationData = namedtuple('PublicationData', ['content_path', 'abstract', 'coauthors'])


publications_title_to_data = {
    'Quantum homogeneous spaces of connected Hopf algebras':
        PublicationData(content_path='https://www.sciencedirect.com/science/article/pii/S0021869316000673',
                        abstract="""Let H be a connected Hopf k-algebra of finite Gel'fand–Kirillov dimension
                                    over an algebraically closed field k of characteristic 0. The objects of
                                    study in this paper are the left or right coideal subalgebras T of H.
                                    They are shown to be deformations of commutative polynomial k-algebras.
                                    A number of well-known homological and other properties follow immediately
                                    from this fact. Further properties are described, examples are considered,
                                    invariants are constructed and a number of open questions are 
                                    listed.""",
                        coauthors="Ken Brown")
}