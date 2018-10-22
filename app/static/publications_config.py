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
                        coauthors="Ken Brown"),

    'Connected (graded) Hopf algebras':
        PublicationData(content_path='https://arxiv.org/abs/1601.06687',
                        abstract="""We study algebraic and homological properties of two classes of infinite
                                     dimensional Hopf algebras over an algebraically closed field k of characteristic zero.
                                      The first class consists of those Hopf k-algebras that are connected graded as
                                       algebras, and the second class are those Hopf k-algebras that are connected as
                                       coalgebras. For many but not all of the results presented here, the Hopf algebras
                                        are assumed to have finite Gel'fand-Kirillov dimension. It is shown that if the
                                         Hopf algebra H is a connected graded algebra of finite Gel'fand-Kirillov
                                          dimension n, then H is a noetherian domain which is Cohen-Macaulay,
                                          Artin-Schelter regular and Auslander regular of global dimension n.
                                          It has S^2 = Id_H, and is Calabi-Yau. Detailed information is also provided
                                           about the Hilbert series of H. Our results leave open the possibility that
                                           the first class of algebras is (properly) contained in the second. For this
                                           second class, the Hopf k-algebras of finite Gel'fand-Kirillov dimension n
                                           with connected coalgebra, the underlying coalgebra is shown to be
                                           Artin-Schelter regular of global dimension n. Both these classes of Hopf
                                            algebra share many features in common with enveloping algebras of finite
                                            dimensional Lie algebras. For example, an algebra in either of these classes
                                             satisfies a polynomial identity only if it is a commutative polynomial
                                             algebra. Nevertheless, we construct, as one of our main results, an
                                              example of a Hopf k-algebra H of Gel'fand-Kirillov dimension 5, which is
                                              connected graded as an algebra and connected as a coalgebra, but is not
                                              isomorphic as an algebra to U(g) for any Lie algebra g.""",
                        coauthors="Ken Brown, James Zhang"),

    'Hopf algebras under finiteness conditions':
        PublicationData(content_path='http://pjm.ppu.edu/vol_3_3/3.pdf',
                        abstract="""This is a brief survey of some recent developments in the study of infinite dimensional
                                    Hopf algebras which are either noetherian or have finite Gelfand-Kirillov dimension. A
                                    number of open questions are listed.""",
                        coauthors="Ken Brown"),

    'A note on the order of the antipode of a pointed Hopf algebra':
        PublicationData(content_path='https://arxiv.org/abs/1611.03480',
                        abstract="""Let k be a field and let H denote a pointed Hopf k-algebra with
                                    antipode S. We are interested in determining the order of S. Building on the
                                     work done by Taft and Wilson [7], we define an invariant for H, denoted mH,
                                     and prove that the value of this invariant is connected to the order of S.
                                     In the case where chark=0, it is shown that if S has finite order then it is
                                     either the identity or has order 2mH. If in addition H is assumed to be
                                     coradically graded, it is shown that the order of S is finite if and only
                                      if mH is finite. We also consider the case where chark=p>0, generalising
                                      the results of [7] to the infinite-dimensional setting.""",
                        coauthors="",
                        ),
}
