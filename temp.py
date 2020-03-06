óÔ-  ã               @   sÈ   G d d dZ dd Zdd Zdd ZG dd	 d	Zd
d Zdd Zdd Zdd Zdd Z	dd Z
dd ZddlZddlZddlZdd Zd(ddZdd  Zd!d" Zd#d$ Zd)d%d&Zde_d'e_dS )*c               @   sT   e Zd Ze i fddZdd Zdd Zdd Zd	d
 Zdd Z	dd Z
dd ZdS )Ú_Vecc             C   s   || _ || _d S )N)ÚDÚf)ÚselfÚlabelsÚfunction© r   ú../resources/private/solver.pyÚ__init__   s    z_Vec.__init__c             C   s   || j kr| j | S dS )Né    )r   )ÚvÚkr   r   r   Ú__getitem__   ó    z_Vec.__getitem__c             C   s   || j |< d S )N)r   )r   r   Úvalr   r   r   Ú__setitem__   r   z_Vec.__setitem__c                s    t | j fdd| jj D S )Nc                s   i | ]\}} | |qS r   r   )Ú.0r   Úx)Úalphar   r   ú
<dictcomp>	   s    z!_Vec.__rmul__.<locals>.<dictcomp>)r   r   r   Úitems)r   r   r   )r   r   Ú__rmul__	   r   z_Vec.__rmul__c             C   s   d|  S )Né   éÿÿÿÿr   )r   r   r   r   Ú__neg__
   r   z_Vec.__neg__c                s0   t  tr(t fddjj D S tS d S )Nc                s   g | ]}|  |  qS r   r   )r   r   )Úotherr   r   r   ú
<listcomp>   s    z _Vec.__mul__.<locals>.<listcomp>)Ú
isinstancer   Úsumr   ÚkeysÚNotImplemented)r   r   r   )r   r   r   Ú__mul__   s    
z_Vec.__mul__c                s2   t  j fddt jj jjj D S )Nc                s   i | ]} | |  |qS r   r   )r   r   )Úur   r   r   r      s    z _Vec.__add__.<locals>.<dictcomp>)r   r   Úsetr   r   Úunion)r!   r   r   )r!   r   r   Ú__add__   r   z_Vec.__add__c             C   s
   | |  S )Nr   )ÚaÚbr   r   r   Ú__sub__   r   z_Vec.__sub__N)Ú__name__Ú
__module__Ú__qualname__r"   r	   r   r   r   r   r    r$   r'   r   r   r   r   r      s   r   c             C   s\   |j d | j kstt|j d i }x2|jj D ]$\\}}}||  | | | 7  < q0W |S )Nr
   r   )r   ÚAssertionErrorr   r   r   )r   ÚMÚresultÚrÚcr   r   r   r   Ú_vector_matrix_mul   s
    r0   c             C   s\   | j d |j kstt| j d i }x2| jj D ]$\\}}}||  || | 7  < q0W |S )Nr   r
   )r   r+   r   r   r   )r,   r   Úresr.   r/   r   r   r   r   Ú_matrix_vector_mul   s
    r2   c          	   C   s   | j d |j d kstt| j d |j d fi }x`| jj D ]R\}}xH|j d D ]:}||f|jkrR|||f  | ||f |||f  7  < qRW q>W |S )Nr   r
   )r   r+   Ú_Matr   r   )ÚAÚBr1   r.   r   r/   r   r   r   Ú_matrix_matrix_mul!   s    0r6   c               @   s<   e Zd Zdd Zdd Zdd Zdd Zd	d
 Zdd ZdS )r3   c             C   s   || _ || _d S )N)r   r   )r   r   r   r   r   r   r	   -   s    z_Mat.__init__c             C   s   || j kr| j | S dS )Nr
   )r   )r   r   r   r   r   r   1   r   z_Mat.__getitem__c             C   s   t  | j|< }d S )N)Z_setitemr   )r   r   r   r   r   r   r   2   r   z_Mat.__setitem__c             C   s*   t | jd | jd fdd | jj D S )Nr   r
   c             S   s   i | ]\\}}}|||fqS r   r   )r   r.   r/   r   r   r   r   r   3   s    z"_Mat.transpose.<locals>.<dictcomp>)r3   r   r   r   )r,   r   r   r   Ú	transpose3   r   z_Mat.transposec          	   C   sä   t t|krt | jd tjd fi }x`| jj D ]R\}}xHtjd D ]:}||ftjkrF|||f  | ||f t||f  7  < qFW q2W |S tt|kràt| jd i }x2| jj D ]$\\}}}||  || | 7  < q´W |S d S )Nr
   r   )r3   Útyper   r5   r   r   r   r   )r4   r   r1   r.   r   r/   r   r   r   r   r    5   s    0z_Mat.__mul__c             C   sX   t t|krTt tjd i }x2tjj D ]$\\}}}||  t| | 7  < q(W |S d S )Nr   )r   r8   r,   r   r   r   r   )r   r   r-   r.   r/   r   r   r   r   r   D   s
    z_Mat.__rmul__N)	r(   r)   r*   r	   r   r   r7   r    r   r   r   r   r   r3   ,   s   r3   c             C   s   t | tr| j S tt| S )z«Given a dict, returns something that generates the keys; given a list,
       returns something that generates the indices.  Intended for coldict2mat and rowdict2mat.
    )r   Údictr   ÚrangeÚlen)Údr   r   r   Ú_keysK   s    r=   c             C   s"   t | trtt| j S | d S )zoGiven either a dict or a list, returns one of the values.
       Intended for coldict2mat and rowdict2mat.
    r
   )r   r9   ÚnextÚiterÚvalues)r<   r   r   r   Ú_valueQ   s    rA   c                s    fdd j d D S )Nc                s4   i | ], t jd   fddjd  D  qS )r   c                s   i | ]} |f |qS r   r   )r   Úcol)r4   Úrowr   r   r   X   s    z+_mat2rowdict.<locals>.<dictcomp>.<dictcomp>)r   r   )r   )r4   )rC   r   r   X   s    z _mat2rowdict.<locals>.<dictcomp>r
   )r   )r4   r   )r4   r   Ú_mat2rowdictW   s    rD   c                s    fdd j d D S )Nc                s4   i | ], t jd   fddjd  D  qS )r
   c                s   i | ]} |f |qS r   r   )r   rC   )r4   rB   r   r   r   [   s    z+_mat2coldict.<locals>.<dictcomp>.<dictcomp>)r   r   )r   )r4   )rB   r   r   [   s    z _mat2coldict.<locals>.<dictcomp>r   )r   )r4   r   )r4   r   Ú_mat2coldictZ   s    rE   c                s4   t  jttt f fddt D S )Nc                s(   i | ] }D ]} | | ||fqqS r   r   )r   r/   r.   )ÚcoldictÚ
row_labelsr   r   r   _   s    z _coldict2mat.<locals>.<dictcomp>)rA   r   r3   r"   r=   )rF   r   )rF   rG   r   Ú_coldict2mat]   s    
rH   c                s4   t j ttt f fddtD S )Nc                s(   i | ] } D ]}| | ||fqqS r   r   )r   r.   r/   )Ú
col_labelsÚrowdictr   r   r   c   s    z _rowdict2mat.<locals>.<dictcomp>)rA   r   r3   r"   r=   )rJ   r   )rI   rJ   r   Ú_rowdict2mata   s    
rK   c             C   sX   t t|i }xDttt| D ]0}|| }| | }|| ||  ||  ||< q W |S )N)r   r"   Úreversedr:   r;   )ZrowlistZ
label_listr&   r   r.   r/   rC   r   r   r   Ú_triangular_solvee   s     rM   r
   Nc             C   s   t t|| S )N)r9   Úzip)ÚLZkeylistr   r   r   Ú
_list2dictq   r   rP   çVç¯Ò<c                sP  t | jd td}t| }g }g }g }g }x|D ]}	||	 }
t|di}x@tt|D ]0}|| }|
| ||  }|||< |
||  }
qVW |
|
 }||kr0|j| |j|
 |j| |j|	 q0W t|}ttt| t	tt
 fdd|D |}|j | }x(|jd D ]}||  ||   < qW t|||}| jd |_|S )Nr   )Úkeyc                s   g | ]}t  |qS r   )r   )r   r   )ÚR_row_label_setr   r   r      s    z_R_solve.<locals>.<listcomp>)Úsortedr   ÚreprrE   r;   r:   ÚappendrH   r"   rD   rP   r7   rM   )r4   r&   ÚepsÚcol_label_listZ	A_coldictZQlistZRlistZ	Q_normsqsZR_col_label_listr/   ZnewvZ	sigmadictÚir   ZsigmaÚnÚQZ	R_rowdictZrhsr   r   )rS   r   Ú_R_solves   s:    



 r\   c             C   s&   x |D ]}| | | |  | |< qW d S )Nr   )Zrow_dictZ	which_rowZrow_index_setZ	row_indexr   r   r   Ú	_add_rows   s    
r]   c                s¦  | j \}}t|td}t|td}t|  t||fdd |D }t|}g }g }	|j }
x~|D ]v fdd|
D }|g kr`|d }|
j| |j |  |	j||  t ||dd   t|||dd   q`W t	|	}t	|t
j d }d}t
|}g xZt|D ]N}x.||k rD||| f dkrD|d7 }qW ||k rj||  qW tfddt|D }t||| }j d |_ |S )	N)rR   c             S   s   i | ]}t j||fqS r   )ÚGF2Zone)r   r.   r   r   r   r      s    z_GF2_solve.<locals>.<dictcomp>c                s    g | ]} |  d kr|qS )r
   r   )r   r.   )Ú	A_rowdictr/   r   r   r   ¡   s    z_GF2_solve.<locals>.<listcomp>r
   r   c                s&   g | ] t  fd dD qS )c                s   i | ]} |f |qS r   r   )r   r/   )ÚUrY   r   r   r   ³   s    z)_GF2_solve.<locals>.<listcomp>.<dictcomp>)r   )r   )r`   Únew_colsÚnew_cols_set)rY   r   r   ³   s    )r   rT   rU   rD   r3   ÚcopyÚremoverV   r]   rK   r;   r:   r"   rM   )r4   r&   rG   rI   Zrow_label_listrX   r,   Z	M_rowdictZ
new_U_rowsZ
new_M_rowsZ	rows_leftZrows_with_nonzeroZpivotZM1ÚmÚjrZ   rY   Z
U1_rowlistr   r   )r_   r`   r/   ra   rb   r   Ú
_GF2_solve   sD    


" 
 rg   c             C   s   t j| j| jS )N)ÚvecÚVecr   r   )r   r   r   r   Ú_convert¸   r   rj   c             C   s¶   t | tjstt |tjs t| jd |jks4tt jd7  _t	| j| j
} t|j|j
}xD|j
j D ]6}|dkrjt |tjrtt| |S tt| ||S qjW tj| jd i S )a#  Solve the matrix-vector equation Ax = b.
    
    If a solution to Ax = b does not exist, then the vector returned by
    solve(A, b) is not a solution.  Please verify that Ax = b.
    
    Args:
        A: A matrix of type Mat.
        b: A vector of type Vec.
        eps: A threshold.  Optional.
    
    Returns:
        x: A vector of type Vec.
    
    Raises:
        AssertionError: An error occurs when A is not a matrix of type Mat.
        AssertionError: An error occurs when b is not a vector of type Vec.
        AssertionError: An error occurs when A.D[0] != b.D.
    
    Example 1: Solve Ax = b and verify that x is close to b.
    >>> from vec import Vec
    >>> from mat import Mat
    >>> A = mat.Mat(({0, 1, 2}, {0, 1}), {(0, 1): 2, (2, 0): 10, (1, 0): 3, (0, 0): 1, (1, 1): 4})
    >>> b = vec.Vec({0, 1, 2},{0: 1, 1: 5, 2: 30})
    >>> A.D[0] == b.D
    True
    >>> x = solve(A, b)
    >>> A.D[1] == x.D
    True
    >>> (b-A*x).is_almost_zero()
    True
    
    Example 2: Solve Ax = b and see that x is not a valid solution.
    >>> A = mat.Mat(({0, 1}, {0, 1}), {(1, 1): 1})
    >>> b = vec.Vec({0, 1},{0: 2, 1: 3})
    >>> A.D[0] == b.D
    True
    >>> x = solve(A, b)
    >>> A.D[1] == x.D
    True
    >>> (b-A*x).is_almost_zero()
    False

    Example 3: Solve when A and b are over GF(2).
    >>> from GF2 import one
    >>> A = Mat(({'a','b'},{'A','B'}), {('a','A'):one, ('a','B'):one, ('b','B'):one})
    >>> b = Vec({'a','b'}, {'a':one})
    >>> x = solve(A, b)
    >>> A*x==b
    True
    >>> (b-A*x).is_almost_zero()
    True

    r
   r   )r   ÚmatZMatr+   rh   ri   r   ÚsolveÚ	__calls__r3   r   r   r@   r^   ZOnerj   rg   r\   )r4   r&   rW   r   r   r   r   rl   º   s    6rl   Zinstrumented)rQ   )rQ   )r   r0   r2   r6   r3   r=   rA   rD   rE   rH   rK   rM   rk   rh   r^   rP   r\   r]   rg   rj   rl   rm   Ú__version__r   r   r   r   Ú<module>   s,   
"
D